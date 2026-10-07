# Submission — HRC Software Onboarding Fall 2026

**Name: Edward Simpson**
**Discord handle: esimpson07**
**Repository: github.com/esimpson07/onboarding-fall26**
**Date: 10/7/2026**

---

## Stage checklist

- [X] **Stage 0** — Setup. `scripts/check_setup.py` exits 0.
- [X] **Stage 1** — MuJoCo + PD controller. Tests green.
- [X] **Stage 2** — JAX exercises. Tests green.
- [X] **Stage 3** — MJX environment. Tests green.
- [X] **Stage 4** — Brax PPO. Trained a policy, exported it, `NumpyPolicy` matches.
- [X] **Stage 5** — ROS 2 sim2sim. Smoke test green, teleop GIF recorded.

## `scripts/progress.py` output

<details>
<summary>paste the full output here</summary>

```
esimpson07@DESKTOP-GV4JLLR:~/onboarding-fall26$ uv run python scripts/progress.py --slow
$ /home/esimpson07/onboarding-fall26/.venv/bin/python -m pytest -q --tb=no -m not gpu and not ros

....................................                                                                             [100%]
=================================================== warnings summary ===================================================
.venv/lib/python3.11/site-packages/jaxopt/__init__.py:59
  /home/esimpson07/onboarding-fall26/.venv/lib/python3.11/site-packages/jaxopt/__init__.py:59: DeprecationWarning: JAXopt is no longer maintained. See https://docs.jax.dev/en/latest/ for alternatives.
    warnings.warn(

tests/test_04_train_smoke.py::test_cpu_smoke
  /home/esimpson07/onboarding-fall26/.venv/lib/python3.11/site-packages/brax/training/agents/ppo/train.py:756: DeprecationWarning: jax.device_put_replicated is deprecated; use jax.device_put instead.
    training_state = jax.device_put_replicated(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

Pup onboarding progress
  ✓ PASSED        Stage 1  MuJoCo + PD controller    12 passed, 0 failed, 0 not started, 0 skipped
  ✓ PASSED        Stage 2  JAX for robotics          9 passed, 0 failed, 0 not started, 0 skipped
  ✓ PASSED        Stage 3  MJX environment           11 passed, 0 failed, 0 not started, 0 skipped
  ✓ PASSED        Stage 4  Brax PPO + export         4 passed, 0 failed, 0 not started, 0 skipped
36 passed, 1 skipped, 2 deselected, 2 warnings in 322.88s (0:05:22)

==============================================================================
PUP ONBOARDING PROGRESS
==============================================================================
✓ PASSED         Stage 1  MuJoCo + PD controller    12 passing
✓ PASSED         Stage 2  JAX for robotics          9 passing
✓ PASSED         Stage 3  MJX environment           11 passing
✓ PASSED         Stage 4  Brax PPO + export         4 passing
◻ CONTAINER      Stage 5  ROS 2 sim2sim             run tests/test_05_ros2_smoke.sh inside docker/ros2
==============================================================================
Every TODO(student) block is written. Nice.
```

</details>

## Stage 4 — training results

**Config used: t4_fast** (`full` / `t4_fast` / other) &nbsp; **Seed: 127** &nbsp;
**Where it ran: Colab T4** (Colab T4 / local GPU / …) &nbsp; **Wall-clock: ~11 min**

Learning curve: `results/learning_curve.png`
Rollout GIF: `results/training.gif`

```json
{
  "seed": 127,
  "n_episodes": 5,
  "commands": [
    {
      "command": [
        0.5,
        0.0,
        0.0
      ],
      "mean_abs_error": [
        0.06454009788036347,
        0.046025757357754625,
        0.09103272300207754
      ],
      "mean_abs_vy": 0.04602575674653053,
      "mean_speed": 0.5374125838279724,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    },
    {
      "command": [
        1.0,
        0.0,
        0.0
      ],
      "mean_abs_error": [
        0.0749770907215774,
        0.05128418876719661,
        0.09585428995248513
      ],
      "mean_abs_vy": 0.05128418654203415,
      "mean_speed": 0.9987626671791077,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    },
    {
      "command": [
        0.0,
        0.5,
        0.0
      ],
      "mean_abs_error": [
        0.05491052736719139,
        0.08051115104258061,
        0.08796620472442591
      ],
      "mean_abs_vy": 0.5632452368736267,
      "mean_speed": 0.567405104637146,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    },
    {
      "command": [
        0.0,
        0.0,
        1.0
      ],
      "mean_abs_error": [
        0.04674873031504976,
        0.054409492721071,
        0.11590752575397491
      ],
      "mean_abs_vy": 0.05440949648618698,
      "mean_speed": 0.0796932652592659,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    },
    {
      "command": [
        0.0,
        0.0,
        0.0
      ],
      "mean_abs_error": [
        0.04790207846453704,
        0.03984605422074092,
        0.08846616892739258
      ],
      "mean_abs_vy": 0.03984605520963669,
      "mean_speed": 0.06880255043506622,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    }
  ],
  "walking_passes": true
}
```

Did it meet the acceptance criteria (`"walking_passes": true`)?

Yes

## Stage 5 — sim2sim results

Teleop GIF: `results/sim2sim_teleop.gif`
Full-quality recording: `results/sim2sim_teleop.mp4`

```json
{
  "duration_s": 20.0,
  "min_trunk_height": 0.29123969534736677,
  "fell": false,
  "commands": [
    {
      "command": [
        0.5,
        0.0,
        0.0
      ],
      "n_samples": 151,
      "mean_velocity": [
        0.38255664716707244,
        0.007591736120324785,
        0.0033023148344842788
      ],
      "mean_abs_error": [
        0.11744335283292756,
        0.007591736120324785,
        0.0033023148344842788
      ],
      "mean_speed": 0.38271344126364765,
      "threshold": 0.25,
      "passed": true
    },
    {
      "command": [
        1.0,
        0.0,
        0.0
      ],
      "n_samples": 150,
      "mean_velocity": [
        0.9563430740347153,
        -0.0032008029596720697,
        -0.008117051912740637
      ],
      "mean_abs_error": [
        0.0436569259652847,
        0.0032008029596720697,
        0.008117051912740637
      ],
      "mean_speed": 0.9566397773035574
    },
    {
      "command": [
        0.0,
        0.0,
        1.0
      ],
      "n_samples": 150,
      "mean_velocity": [
        -0.08885892394035899,
        0.07468173297696931,
        0.9907010239548142
      ],
      "mean_abs_error": [
        0.08885892394035899,
        0.07468173297696931,
        0.009298976045185814
      ],
      "mean_speed": 0.1179064701930696
    },
    {
      "command": [
        0.0,
        0.0,
        0.0
      ],
      "n_samples": 150,
      "mean_velocity": [
        0.0001709993389772682,
        0.00011948192756598019,
        0.00026021182705369256
      ],
      "mean_abs_error": [
        0.0001709993389772682,
        0.00011948192756598019,
        0.00026021182705369256
      ],
      "mean_speed": 0.004483975535409149
    }
  ],
  "passed": true
}
```

Measured `/pup/joint_command` rate from `ros2 topic hz`:

## Escape hatches used

- [X] I used `checkpoints/pup_joystick_flat_reference.npz` for Stage 5 instead
      of my own policy.
- [ ] Other (describe):

*(Using one is fine. Not declaring one is not.)*

## Reflection — Stage 5

**List two ways sim2sim can pass while real hardware still fails, and what you
would add to the sim node to catch each.**

1. The motor messages can send with latency as opposed to the simulation's perfect response times. One way we could fix this in the sim is adding latency to the sim node in order to simulate how the real hardware would act. This would then make the training better match the real motor response, and would prevent aggressive oscillation due to delayed responses.

2. The IMU responses could actually drift in real life, making the robot think it may be moving when it's not. In order to counteract this, we could add noise to the sim node on the IMU signal, making the noise random so that it will cause the robot's IMU responses to drift. 
> 

## What was hardest?

One paragraph. This is will help us improve onboarding.

For me, step 3 was the hardest. This one was the most code writing, but I also found it the hardest to understand conceptually. However, I think I mostly understood it, but trying to get all of the jax method's syntax correct was a challenge for me. I am very unfamiliar with jax so this was quite challenging. 
>

## Time spent

| Stage | Hours |
|---|---|
| 0 Setup         |1.5|
| 1 MuJoCo + PD   |1.0|
| 2 JAX           |1.5|
| 3 MJX env       |2.0|
| 4 Brax + export |1.0|
| 5 ROS 2         |1.5|
| **Total**       |8.5|

---

**Then DM the software lead (Henry Tsay) on Discord or show during a meeting.**
