import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import Book
from authentication.models import CustomUser
from order.models import Order



def orders_list(request):
    if request.user.is_authenticated:
        if request.user.is_staff:  
            orders = Order.get_all()
        else:  
            orders = Order.objects.filter(user=request.user)
        return render(request, 'order/orders_list.html', {'orders': orders})
    else:
        return HttpResponse('Unauthorized', status=401)


def create_order(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        user_id = request.POST.get('user_id')
        try:
            book = Book.objects.get(pk=book_id)
            user = CustomUser.objects.get(pk=user_id)
            plated_end_at = datetime.datetime.now() + datetime.timedelta(weeks=2)
            order = Order.create(user=user, book=book, plated_end_at=plated_end_at)
            if order:
                return redirect('orders_list')
            else:
                return HttpResponse('Unable to create order.', status=400)
        except Book.DoesNotExist:
            return HttpResponse('Book not found.', status=404)
        except CustomUser.DoesNotExist:
            return HttpResponse('User not found.', status=404)
    return render(request, 'order/create_order.html')


def close_order(request, order_id):
    if request.method == 'POST' and request.user.is_staff:
        try:
            order = Order.get_by_id(order_id)
            if order:
                order.update(end_at=datetime.datetime.now())
                return redirect('orders_list')
            else:
                return HttpResponse('Order not found.', status=404)
        except Exception as e:
            return HttpResponse(f'Error: {e}', status=400)
    return HttpResponse('Unauthorized', status=403)