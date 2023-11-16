from django.db import models


class Components(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ComponentsAbout(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='components', null=True, blank=True)
    component_id = models.ForeignKey(
        Components, on_delete=models.CASCADE, null=True, blank=True)
    files = models.FileField(upload_to='files', null=True, blank=True)

    def __str__(self):
        return self.title
