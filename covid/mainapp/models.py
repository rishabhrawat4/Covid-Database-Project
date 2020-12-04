from django.db import models

class Drug(models.Model):
    drugbankId = models.CharField(max_length=200)
    pubchemId = models.CharField(max_length=200)
    drugName = models.CharField(max_length=200)
    pmid = models.CharField(max_length=200)
    approvedAgainstDiseases = models.CharField(max_length=200, blank=True, null=True)
    diseaseMeshId = models.CharField(max_length=200, blank=True, null=True)
    mechanismOfAction = models.CharField(max_length=3000, blank=True, null=True)
    geneTargets = models.CharField(max_length=200)
    uniportId = models.CharField(max_length=200)
    geneSymbol = models.CharField(max_length=200)

    


