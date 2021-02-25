from django.db import models
from authentication import models as models_auth


class CheckInOut(models.Model): 
    user = models.ForeignKey(to=models_auth.User, on_delete=models.CASCADE, null=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    def __str__(self): 
        return f"{self.user} {self.check_in}-{self.check_out}"
 

    
    


