from django.db import models

# Create your models here.
# SCJourney/models.py

from django.db import models

class Milestone(models.Model):
    """
    Model representing a key achievement or milestone in the learning journey.
    This fulfills the 'create models' requirement.
    """
    title = models.CharField(max_length=200, help_text="A brief title for the milestone.")
    description = models.TextField(help_text="Detailed description of what was learned or achieved.")
    date_achieved = models.DateField(help_text="The date this milestone was completed.")

    def str(self):
        # Returns the title in the admin interface for readability
        return self.title