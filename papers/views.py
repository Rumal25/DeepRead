from django.shortcuts import render


def home(request):
    return render(request, 'papers/home.html')


def paper_list(request):
    # DUMMY DATA — no database yet
    dummy_papers = [
        {'id': 1, 'title': 'Proximal Policy Optimization', 'authors': 'Schulman et al.',
         'year': 2017, 'status': 'Implemented', 'rating': 5},
        {'id': 2, 'title': 'Soft Actor-Critic', 'authors': 'Haarnoja et al.',
         'year': 2018, 'status': 'Read', 'rating': 4},
        {'id': 3, 'title': 'Deep Q-Network', 'authors': 'Mnih et al.',
         'year': 2015, 'status': 'To Read', 'rating': 0},
    ]
    return render(request, 'papers/paper_list.html', {'papers': dummy_papers})


def paper_detail(request, pk):
    # DUMMY DATA for one paper
    dummy_paper = {
        'id': pk,
        'title': 'Proximal Policy Optimization',
        'authors': 'Schulman et al.',
        'year': 2017,
        'venue': 'arXiv',
        'arxiv_id': '1707.06347',
        'status': 'Implemented',
        'rating': 5,
    }
    dummy_notes = [
        {'content': 'Clipped surrogate objective is key', 'page_number': 3},
        {'content': 'Compare with TRPO results', 'page_number': 7},
    ]
    return render(request, 'papers/paper_detail.html', {
        'paper': dummy_paper,
        'notes': dummy_notes,
    })


def paper_form(request):
    return render(request, 'papers/paper_form.html')