"""
_summary_
"""

from behavysis_core.data_models.pydantic_base_model import PydanticBaseModel
from pydantic import ConfigDict


class BehavClassifierConfigs(PydanticBaseModel):
    """_summary_"""

    model_config = ConfigDict(extra="forbid")

    train_fraction: float = 0.8
    undersampling_strategy: float = 1.0
    seed: int = 42
    pcutoff: float = 0.15
    all_ls: list[str] = []
    train_ls: list[str] = []
    test_ls: list[str] = []
    name: str = "Base"

    model_type: str = "RandomForestClassifier"
    model_params: dict = {
        "n_estimators": 2000,
        "learning_rate": 0.1,
        "loss": "log_loss",
        "criterion": "friedman_mse",
        "max_features": "sqrt",
        "random_state": seed,
        "subsample": 1.0,
        "verbose": 1,
    }
