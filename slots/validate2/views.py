import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def validate_numeric_entity(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response = {
                        'filled': False,
                        'partially_filled': False,
                        'trigger': "",
                        'parameters': {}
                    }
            valid = len(data['values']) > 0
            pick_first = 'pick_first' in data and data['pick_first']
            multiple = 'support_multiple' in data and data['support_multiple']
            constraint = 'constraint' in data and len(data['constraint']) > 0

            if pick_first == multiple:
                raise Exception('pick_first and support_multiple exception')
            else:
                if pick_first:
                    if valid and (constraint == False or eval(data['constraint'], {}, {data['var_name']: data['values'][0]['value']})):
                        response['parameters'] = {data['key']: data['values'][0]['value']}
                    
                for entity in data['values']:
                    if constraint and eval(data['constraint'], {}, {data['var_name']: entity['value']}) == False:
                        response['partially_filled'] = True
                        valid = False
                    elif multiple:
                        response['parameters'].setdefault(data['key'], []).append(entity['value'])
                    
                if valid == True:
                    response['filled'] = True
                else:
                    response['trigger'] = data['invalid_trigger']

                return JsonResponse(response, status=200)
    
        except Exception as e:
            return JsonResponse({'status': 'failed', 'message': 'invalid_request', 'error': str(e)}, status=406)

    return JsonResponse({})