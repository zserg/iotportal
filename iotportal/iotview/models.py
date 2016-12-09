from django.db import models

class IotView(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    view_type = models.CharField(max_length=255)
    node0_path = models.CharField(max_length=1024)
    node1_path = models.CharField(max_length=1024, default='', blank=True)
    node2_path = models.CharField(max_length=1024, default='', blank=True)
    node3_path = models.CharField(max_length=1024, default='', blank=True)
    node0_descr = models.CharField(max_length=255)
    node1_descr = models.CharField(max_length=255, default='', blank=True)
    node2_descr = models.CharField(max_length=255, default='', blank=True)
    node3_descr = models.CharField(max_length=255, default='', blank=True)


    def get_last_value_url(self):
        """
        get API url from nodex_path:
        'dev_id!node_path'
        """
        base_url = 'data/read/{}?datanodes={}'
        paths = []
        paths.append((self.node0_descr, base_url.format(*self.node0_path.split('!'))))
        if self.node1_path:
            paths.append((self.node1_descr, base_url.format(*self.node1_path.split('!'))))
        if self.node2_path:
            paths.append((self.node2_descr, base_url.format(*self.node2_path.split('!'))))
        if self.node3_path:
            paths.append((self.node3_descr, base_url.format(*self.node3_path.split('!'))))

        return paths

class API(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


