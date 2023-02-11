from django.db import models

from .plan import Plan


class Organization(models.Model):
    """
    Organization model

    Relations:
        Has many Membership
        Has many Plan
        Has many Company
    """
    # Relations
    plans = models.ManyToManyField(Plan, through='PlanOrganization')

    # Fields
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self) -> str:
        return self.name
