from django.db import models
from django.utils import timezone


class Author(models.Model):
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        db_table = 'author'
        ordering = ['last_name']

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Topic(models.Model):
    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        db_table = 'topic'
        ordering = ['name']

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Paper(models.Model):
    class Meta:
        verbose_name = 'Paper'
        verbose_name_plural = 'Papers'
        db_table = 'paper'
        ordering = ['-year']

    STATUS_CHOICES = [
        ('toread', 'To Read'),
        ('reading', 'Reading'),
        ('read', 'Read'),
        ('implemented', 'Implemented'),
    ]

    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    title = models.CharField(max_length=300)
    authors = models.ManyToManyField(Author, blank=True)
    year = models.IntegerField(default=2024)
    venue = models.CharField(max_length=200, blank=True, null=True)
    arxiv_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='toread'
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=0,
        blank=True,
        null=True
    )
    topics = models.ManyToManyField(Topic, blank=True)
    abstract = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Citation(models.Model):
    class Meta:
        verbose_name = 'Citation'
        verbose_name_plural = 'Citations'
        db_table = 'citation'
        unique_together = ('citing_paper', 'cited_paper')

    citing_paper = models.ForeignKey(
        Paper,
        related_name='citations_out',
        on_delete=models.CASCADE
    )
    cited_paper = models.ForeignKey(
        Paper,
        related_name='citations_in',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.citing_paper.title} → {self.cited_paper.title}"


class ReadingNote(models.Model):
    class Meta:
        verbose_name = 'Reading Note'
        verbose_name_plural = 'Reading Notes'
        db_table = 'reading_note'
        ordering = ['page_number']

    paper = models.ForeignKey(
        Paper,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    content = models.TextField()
    page_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Note on {self.paper.title} (p.{self.page_number})"


class Experiment(models.Model):
    class Meta:
        verbose_name = 'Experiment'
        verbose_name_plural = 'Experiments'
        db_table = 'experiment'
        ordering = ['-created_at']

    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    paper = models.ForeignKey(
        Paper,
        on_delete=models.CASCADE,
        related_name='experiments'
    )
    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='planned'
    )
    result_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} ({self.status})"