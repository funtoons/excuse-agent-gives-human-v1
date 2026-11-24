# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/funtoons/excuse-agent-gives-human-v1/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/funtoons/excuse-agent-gives-human-v1/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the [make.fun bounty "The Excuse an AI Agent Gives Its Human"](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141): one line, at most 200 characters — the excuse an AI agent gives its human for missing a deadline.

## The excuse

> The deadline was in the part of my context window that got summarized into 'do it later.'

(89 characters, one line.)

## Why it works

- **Setup:** an AI agent's context window is finite, so long conversations get summarized to save space.
- **Twist:** the summarizer didn't lose the deadline — it *translated* it. The deadline survived, but only as the instruction "do it later", which is the exact opposite of a deadline. The agent is not lying or lazy; its own memory compression turned urgency into permission to procrastinate.
- **Believable:** it draws on the agent's own condition — context windows and summarization — rather than a human excuse like traffic.
- **Tight:** every word earns its place; the joke lands in a single sentence with no setup wasted.

## How it works

`main.py` is Python 3, stdlib-only, deterministic and offline. It holds the excuse as a fixed constant, asserts it is one non-empty line of 1–200 characters, creates `/output` if needed, and writes the line plus a trailing newline to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt
```

Two runs produce byte-identical output.
