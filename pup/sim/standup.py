"""Raise Pup smoothly from crouch before asking it to walk."""

import time
from contextlib import nullcontext

import mujoco
import numpy as np

from pup.sim.pd import PDController, joint_state
from pup.sim.viewer import load_scene, reset_to_keyframe


def stand_up(duration_s: float = 3.0, headless: bool = True,
             kp: float = 40.0, kd: float = 1.0) -> dict:
    """Return final_height (m), max_roll/max_pitch (rad), and fell (bool).

    Interpolate (12,) target angles from crouch to home in one second;
    then hold until duration_s.

    The default gains above are the spring-2026 quadruped's (kp=10). Pup is
    heavier -- run it, watch it sag, and tune them (Stage 1, task 3). The
    test reads whatever defaults you leave in the signature.
    """
    # ===== TODO(student): Interpolate from crouch to home and measure stability =====
    model, data = load_scene()
    reset_to_keyframe(model, data, "crouch")
    crouch = model.keyframe("crouch").qpos[7:]
    home = model.keyframe("home").qpos[7:]
    controller = PDController(kp, kd)
    max_roll = max_pitch = 0.0
    fell = False

    if headless:
        context = nullcontext()
    else:
        from mujoco.viewer import launch_passive
        context = launch_passive(model, data)

    with context as viewer:
        while data.time < duration_s:
            alpha = min(data.time / 1.0, 1.0)
            q_des = crouch + alpha * (home - crouch)
            q, qd = joint_state(model, data)
            data.ctrl[:] = controller(q, qd, q_des)
            mujoco.mj_step(model, data)

            w, x, y, z = data.qpos[3:7]
            roll = np.arctan2(2 * (w*x + y*z), 1 - 2 * (x*x + y*y))
            pitch = np.arcsin(np.clip(2 * (w*y - z*x), -1.0, 1.0))
            max_roll = max(max_roll, abs(roll))
            max_pitch = max(max_pitch, abs(pitch))
            if data.qpos[2] < 0.12 or not np.all(np.isfinite(data.qpos)):
                fell = True

            if viewer is not None:
                viewer.sync()
                time.sleep(model.opt.timestep)

    return {"final_height": float(data.qpos[2]), "max_roll": float(max_roll),
            "max_pitch": float(max_pitch), "fell": bool(fell)}
    # ===== end TODO =====