from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Board
from .forms import BoardForm


# 게시글 목록
@login_required(login_url="common:login")
def board_list(request):
    board_list = Board.objects.order_by("-created_date")

    page = request.GET.get("page", 1)
    paginator = Paginator(board_list, 10)
    object_list = paginator.get_page(page)

    context = {"board_list": object_list}
    return render(request, "board/list.html", context)


# 게시글 등록
@login_required(login_url="common:login")
def board_create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect("board:board_list")
    else:
        form = BoardForm()
    context = {"form": form}
    return render(request, "board/create.html", context)


# 게시글 보기
@login_required(login_url="common:login")
def board_read(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    context = {"board": board}
    return render(request, "board/read.html", context)


# 게시글 수정
@login_required(login_url="common:login")
def board_update(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if board.author != request.user:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect("board:board_read", board_id=board.id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            messages.success(request, "글을 수정하였습니다.")
            return redirect("board:board_read", board_id=board.id)
    else:
        form = BoardForm(instance=board)
    context = {"form": form, "board": board}
    return render(request, "board/update.html", context)


# 게시글 삭제
@login_required(login_url="common:login")
def board_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if board.author != request.user:
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect("board:board_read", board_id=board.id)
    board.delete()
    messages.success(request, "글을 삭제하였습니다.")
    return redirect("board:board_list")
