from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

def homepage(request):
    return render(request, 'index.html') # return home page

def calculate(request): # function for calculation
    if request.method == 'POST':
        try: # exception handling
            numbers = list(map(float, request.POST.getlist('numbers'))) # Get numbers and operation
            operation = request.POST.get('operation')

            if operation == 'add': # Perform the operation
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

            return render(request, 'result.html', {'result': result}) # passes result to result page

        except ValueError:  # invalid input other than number
            return render(request, 'result.html', {
                'error': 'Invalid input. Ensure all inputs are numbers.'
            })

    return HttpResponseBadRequest('Invalid request method.')
