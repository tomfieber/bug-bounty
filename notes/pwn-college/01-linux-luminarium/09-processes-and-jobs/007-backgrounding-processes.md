This level's `run` wants to see another copy of itself running, _not suspended_, and using the same terminal. How? Use the terminal to launch it, then suspend it, then _background_ it with `bg` and launch another copy while the first is running in the background!

```bash
# Run the first challenge
/challenge/run

# Suspend the process
Ctrl+z

# Background the suspended process to resume it but get your shell back
bg

# Run the second instance of the challenge
/challenge/run
```

