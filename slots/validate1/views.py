import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def validate_finite_values_entity(request):
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
            supported = 'supported_values' in data and len('supported_values') > 0

            if pick_first == multiple:
                raise Exception('pick_first and support_multiple exception')

            else:
                for entity in data['values']:
                    if supported and entity['value'] not in data['supported_values']:
                        response['partially_filled'] = True
                        valid = False
                        break

                if valid:
                    response['filled'] = True
                
                    if pick_first:
                        response['parameters'] = {data['key']: data['values'][0]['value'].upper()}

                    if multiple:
                        response['parameters'] = {data['key']: [entity['value'].upper() for entity in data['values']]}
                else:
                    response['trigger'] = data['invalid_trigger']

                return JsonResponse(response, status=200)

        except Exception as e:
            return JsonResponse({'status': 'failed', 'message': 'invalid_request', 'error': str(e)}, status=406)

    return JsonResponse({})