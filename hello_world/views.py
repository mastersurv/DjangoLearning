from django.shortcuts import render
from hello_world.models import Worker


def index_page(request):
    all_workers = Worker.objects.all()  # Получение всех записей из таблицы Worker
    print(all_workers)

    # new_worker = Worker(name='Иван', second_name='Закорюкин', salary=70000)
    # new_worker.save()

    try:
        worker_to_change = Worker.objects.get(id=5)
        worker_to_change.second_name = 'Машиткин'
        worker_to_change.save()
        print(worker_to_change)

    except Exception as e:
        print(e)

    # Удаление
    try:
        Worker.objects.get(id=5).delete()
    except Exception as e:
        print(e)

    workers_filtered = Worker.objects.filter(salary=88000)
    print(workers_filtered)

    for i in all_workers:
        print(f'{i.second_name} {i.name} {i.salary} {i.id}')

    return render(request, 'index.html')