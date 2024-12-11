from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

def homepage(request):
    return render(request, 'index.html')

def calculate(request):
    if request.method == 'POST':
        try:
            # Get numbers and operation from the request
            numbers = list(map(float, request.POST.getlist('numbers')))
            operation = request.POST.get('operation')

            # Perform the operation
            if operation == 'add':
                result = sum(numbers)
            elif operation == 'subtract':
                result = numbers[0] - sum(numbers[1:])
            elif operation == 'multiply':
                result = 1
                for num in numbers:
                    result *= num
            elif operation == 'divide':
                result = numbers[0]
                for num in numbers[1:]:
                    if num == 0:
                        return render(request, 'result.html', {
                            'error': 'Division by zero is not allowed.'
                        })
                    result /= num
            else:
                return render(request, 'result.html', {
                    'error': 'Invalid operation.'
                })

            # Render result page
            return render(request, 'result.html', {'result': result})

        except ValueError:
            return render(request, 'result.html', {
                'error': 'Invalid input. Ensure all inputs are numbers.'
            })

    return HttpResponseBadRequest('Invalid request method.')
