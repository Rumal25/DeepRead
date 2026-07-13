from django.shortcuts import render, redirect, get_object_or_404
from papers.models import Paper, Author, Topic, ReadingNote, Experiment, Citation
from papers.forms import PaperForm, AuthorForm, TopicForm, ReadingNoteForm, ExperimentForm


# ── Home ──────────────────────────────────
def home(request):
    from papers.models import Topic
    total_papers = Paper.objects.count()
    total_experiments = Experiment.objects.count()
    total_topics = Topic.objects.count()
    recent_papers = Paper.objects.order_by('-created_at')[:5]
    context = {
        'total_papers': total_papers,
        'total_experiments': total_experiments,
        'total_topics': total_topics,
        'recent_papers': recent_papers,
    }
    return render(request, 'papers/home.html', context)

# ── Paper List ────────────────────────────
def paper_list(request):
    papers = Paper.objects.all().order_by('-year')
    # Filter by status
    status = request.GET.get('status')
    if status:
        papers = papers.filter(status=status)
    # Filter by topic
    topic_id = request.GET.get('topic')
    if topic_id:
        papers = papers.filter(topics__id=topic_id)
    topics = Topic.objects.all()
    context = {
        'papers': papers,
        'topics': topics,
        'selected_status': status,
        'selected_topic': topic_id,
    }
    return render(request, 'papers/paper_list.html', context)


# ── Paper Detail ──────────────────────────
def paper_detail(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    notes = paper.notes.all().order_by('page_number')
    experiments = paper.experiments.all()
    citations_out = paper.citations_out.all()
    citations_in = paper.citations_in.all()
    all_papers = Paper.objects.exclude(pk=pk)

    if request.method == 'POST':
        # Add citation
        cited_id = request.POST.get('cited_paper')
        if cited_id:
            cited = get_object_or_404(Paper, pk=cited_id)
            Citation.objects.get_or_create(
                citing_paper=paper, cited_paper=cited)
            return redirect('papers:paper_detail', pk=pk)

    context = {
        'paper': paper,
        'notes': notes,
        'experiments': experiments,
        'citations_out': citations_out,
        'citations_in': citations_in,
        'all_papers': all_papers,
    }
    return render(request, 'papers/paper_detail.html', context)


# ── Add / Edit Paper ──────────────────────
def paper_form(request, pk=None):
    paper = get_object_or_404(Paper, pk=pk) if pk else None
    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect('papers:paper_list')
    else:
        form = PaperForm(instance=paper)
    return render(request, 'papers/paper_form.html', {'form': form, 'paper': paper})


# ── Delete Paper ──────────────────────────
def paper_delete(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    paper.delete()
    return redirect('papers:paper_list')


# ── Reading Note ──────────────────────────
def note_add(request, paper_pk):
    paper = get_object_or_404(Paper, pk=paper_pk)
    if request.method == 'POST':
        form = ReadingNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.paper = paper
            note.save()
            return redirect('papers:paper_detail', pk=paper_pk)
    else:
        form = ReadingNoteForm()
    return render(request, 'papers/note_form.html', {'form': form, 'paper': paper})


def note_delete(request, pk):
    note = get_object_or_404(ReadingNote, pk=pk)
    paper_pk = note.paper.pk
    note.delete()
    return redirect('papers:paper_detail', pk=paper_pk)


# ── Experiment ────────────────────────────
def experiment_add(request, paper_pk):
    paper = get_object_or_404(Paper, pk=paper_pk)
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.paper = paper
            exp.save()
            return redirect('papers:paper_detail', pk=paper_pk)
    else:
        form = ExperimentForm()
    return render(request, 'papers/experiment_form.html', {'form': form, 'paper': paper})


def experiment_delete(request, pk):
    exp = get_object_or_404(Experiment, pk=pk)
    paper_pk = exp.paper.pk
    exp.delete()
    return redirect('papers:paper_detail', pk=paper_pk)


# ── Authors ───────────────────────────────
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'papers/author_list.html', {'authors': authors})


def author_form(request, pk=None):
    author = get_object_or_404(Author, pk=pk) if pk else None
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('papers:author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'papers/author_form.html', {'form': form, 'author': author})


# ── Topics ────────────────────────────────
def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'papers/topic_list.html', {'topics': topics})


def topic_form(request, pk=None):
    topic = get_object_or_404(Topic, pk=pk) if pk else None
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('papers:topic_list')
    else:
        form = TopicForm(instance=topic)
    return render(request, 'papers/topic_form.html', {'form': form, 'topic': topic})