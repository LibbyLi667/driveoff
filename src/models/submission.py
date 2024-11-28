"""Classes related to user submission for offboarding."""

from datetime import datetime
from typing import TYPE_CHECKING, Self

from pydantic import ConfigDict, model_validator
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.services import ResearchDriveService

DEFAULT_RETENTION_PERIODS = set([6, 10, 20, 26])


class DriveOffboardSubmission(SQLModel, table=True):
    """Model that represents a user's submission in the drive offboarding process."""

    # Bug with SQLModel library causing typing error:
    # https://github.com/fastapi/sqlmodel/discussions/855
    model_config = ConfigDict(str_strip_whitespace=True)  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    retention_period_years: int
    retention_period_justification: str | None
    data_classification: str
    is_completed: bool
    updated_time: datetime
    is_project_updated: bool
    drive_id: int = Field(
        default=None, unique=True, foreign_key="researchdriveservice.id"
    )
    drive: "ResearchDriveService" = Relationship(back_populates="submission")

    @model_validator(mode="after")
    def check_custom_retention_period_has_justification(self) -> Self:
        """Validates that if a submission has a non-default retention period,
        that it should provide a justification."""
        period = self.retention_period_years
        justification = self.retention_period_justification
        justification_is_empty = justification is None or justification == ""
        if period not in DEFAULT_RETENTION_PERIODS and justification_is_empty:
            raise ValueError(
                "Retention period is not a default value, justification needs to be provided."
            )
        return self
