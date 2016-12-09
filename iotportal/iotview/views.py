from django.shortcuts import render
from iotview.models import IotView, API

import requests
import json
from datetime import datetime

API_NAME = 'iot_storage'

def index(request):
    #import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        iot_views = IotView.objects.all()[:10]

        if iot_views:
            api = API.objects.get(name=API_NAME)
            api_token = api.token
            api_url = api.url
            headers = {'Authorization': 'Token {}'.format(api_token)}
            context = {'views':[]}

            for iot in iot_views:
                c_v = {}
                c_v['description'] = iot.description
                c_v['nodes'] = []
                urls = iot.get_last_value_url()
                for url in urls:
                    c_t = {'descr': url[0]}

                    r = requests.get(api_url + url[1], headers=headers)
                    if r.status_code == 200:
                        #c_t['data'] =  r.json()
                        print(r.json())
                        out = r.json()[0]
                        ps = []
                        for point in out['points']:
                            p = {}
                            p['value'] = point['value']
                            p['created_at'] = datetime.fromtimestamp(point['created_at']).strftime('%d.%m %H:%M')
                            ps.append(p)
                    c_t['data'] = ps
                    c_t['status'] = r.status_code
                    c_v['nodes'].append(c_t)
                context['views'].append(c_v)

            print(json.dumps(context))
            return render(request, 'iotview/index.html', context)
        else:
            return render(request, 'iotview/index.html', {'data':'not found'})

