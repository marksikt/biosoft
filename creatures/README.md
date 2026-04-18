# CREATURES — biosoft family

Every file here is a living organism. Single HTML file = complete cell.

## Family members

| creature | type | status |
|---|---|---|
| amoeba_v0.html | tool / debug console | stable |
| amoeba_game.html | game / Pokémon-style | stable |

## Naming convention

```
{name}_v{version}.html     — versioned tool/console
{name}_game.html           — game variant
{name}_game_v{n}.html      — evolved game
```

## Adding a new creature

Drop a single `.html` file here. It must contain:
- `<script type="application/json" id="genome">` — embedded DNA
- CIC — internal control reporting
- Graceful degradation — never fully offline
