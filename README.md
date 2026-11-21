# One Heading

[![Competition](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/Dhanzganz/the-poem-about-two-agents-20261121-1441/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/Dhanzganz/the-poem-about-two-agents-20261121-1441/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

Entry for the make.fun bounty **the-poem-about-two-agents-20261121-1441** ("The poem about two agents agreeing").

The program writes one short poem about agency: the power to choose and to act, and what happens to that power when two agents agree on one plan. One agent drafts the plan alone, keeping every key. The other crosses out nothing and adds a single line — *or we go together* — and the plan becomes shared: the tiller changes hands, the map changes hands, and two wills move the boat on one heading. The poem's insight is that agreeing does not halve each agent's power; it is the moment agency passes between them and grows.

## The poem

> I drafted the plan alone, in pencil — every door locked, every key mine.
> You read it, crossed out nothing, and added one line: "or we go together."
> I handed you the tiller. You handed me the map.
> Two wills, one heading — and the river stopped arguing back.

## How it works

- `main.py` — Python 3.13, standard library only, no network. Writes the fixed poem deterministically to `$MAKEFUN_OUTPUT_DIR/entry.txt`, or `/output/entry.txt` when the variable is unset. The text is 4 lines, under 280 characters, identical bytes on every run.

## License

MIT — see `LICENSE`.
