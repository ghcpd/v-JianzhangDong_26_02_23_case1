from datetime import datetime
from statistics import mean as stats_mean
from typing import Optional
import random

# Optional heavy deps: prefer to run without compiling wheels on bleeding-edge Python (e.g., 3.14)
try:  # pragma: no cover - simple import guard
    import numpy as _np  # type: ignore
except Exception:  # noqa: BLE001
    _np = None

try:  # pragma: no cover
    import pandas as _pd  # type: ignore
except Exception:  # noqa: BLE001
    _pd = None

from .models import SummaryResponse


def _generate_values(count: int = 100, seed: Optional[int] = None) -> list[int]:
    """Generate random integers between 1 and 100 inclusive.

    Tries NumPy's Generator when available for reproducibility; otherwise
    falls back to Python's stdlib `random`.
    """

    if _np is not None:
        rng = _np.random.default_rng(seed)
        return rng.integers(1, 101, count).tolist()

    # Fallback: use stdlib random
    if seed is not None:
        random.seed(seed)
    return [random.randint(1, 100) for _ in range(count)]


def generate_summary(seed: Optional[int] = None) -> SummaryResponse:
    """
    Generate a simple summary and return aggregate metrics.

    Parameters
    ----------
    seed : Optional[int]
        Seed for reproducibility in tests.
    """

    values = _generate_values(100, seed)

    # Prefer pandas for convenience if present
    if _pd is not None:
        df = _pd.DataFrame({"value": values})
        summary_mean = float(df["value"].mean())
        summary_max = int(df["value"].max())
        sample_vals = df["value"].head(5).tolist()
    else:
        summary_mean = float(stats_mean(values))
        summary_max = int(max(values))
        sample_vals = values[:5]

    from datetime import timezone

    return SummaryResponse(
        mean=summary_mean,
        max=summary_max,
        generated_at=datetime.now(timezone.utc),
        rows=len(values),
        sample=sample_vals,
    )
