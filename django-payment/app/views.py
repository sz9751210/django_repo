from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseModelForm
def index(request):

    expenses = Expense.objects.all() # 查詢所有資料 方便顯示

    form = ExpenseModelForm() # 創建一個form 方便等一下接收post請求的傳入資料

    if request.method == "POST":
        # print(request.POST) <QueryDict: {'csrfmiddlewaretoken': ['3Igg5L5OnzIdO8HWF5f0y2pvG7zyUI6iVhpSLYxnDQPTAKd4fEygf9QdQUJEnodg'], 'name': ['e'], 'price': ['3']}>
        form=ExpenseModelForm(request.POST) # 當 Django 接收到 HTTP POST 請求時，它會將表單數據放在 "request.POST" 中。表單數據包含表單字段的名稱和對應的值。
        if form.is_valid():  # 所以，"ExpenseModelForm(request.POST)" 會使用客戶端提交的表單數據創建一個新的表單對象。這使我們可以使用表單類的方法，例如 "is_valid()" 和 "save()"，檢驗表單數據並將其保存到資料庫中。
            form.save() # 保存到db
        return redirect("/app")
    context = {
        'expenses': expenses,
        'form': form
    }
    return render(request, 'app/index.html', context)



def update(request, pk):
    expense=Expense.objects.get(id=pk)

    form = ExpenseModelForm(instance=expense)

    if request.method == "POST":
        # print(request.POST) <QueryDict: {'csrfmiddlewaretoken': ['3Igg5L5OnzIdO8HWF5f0y2pvG7zyUI6iVhpSLYxnDQPTAKd4fEygf9QdQUJEnodg'], 'name': ['e'], 'price': ['3']}>
        form=ExpenseModelForm(request.POST) # 當 Django 接收到 HTTP POST 請求時，它會將表單數據放在 "request.POST" 中。表單數據包含表單字段的名稱和對應的值。
        if form.is_valid():  # 所以，"ExpenseModelForm(request.POST)" 會使用客戶端提交的表單數據創建一個新的表單對象。這使我們可以使用表單類的方法，例如 "is_valid()" 和 "save()"，檢驗表單數據並將其保存到資料庫中。
            form.save() # 保存到db
        return redirect("/app")
    context = {
        'form': form
    }

    return render(request, 'app/update.html', context)

def delete(request, pk):
    expense=Expense.objects.get(id=pk)

    # form = ExpenseModelForm(instance=expense)

    if request.method == "POST":
        # print(request.POST) <QueryDict: {'csrfmiddlewaretoken': ['3Igg5L5OnzIdO8HWF5f0y2pvG7zyUI6iVhpSLYxnDQPTAKd4fEygf9QdQUJEnodg'], 'name': ['e'], 'price': ['3']}>
        expense.delete() # 當 Django 接收到 HTTP POST 請求時，它會將表單數據放在 "request.POST" 中。表單數據包含表單字段的名稱和對應的值。
        return redirect("/app")
    context = { # 這邊還需要context是因為render要顯示名稱
        'expense': expense
    }
    print(context)
    return render(request, 'app/delete.html', context)