import { Component, OnInit } from '@angular/core';
import { Todo } from '../models/todo.model';
import { TodoService } from '../_services/todo.service';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {

  todo?: Todo[];
  currentTodo: Todo = {};
  currentIndex = -1;
  title = '';

  constructor(private TodoService: TodoService) { }

  ngOnInit(): void {
    this.retrieveTodos();
  }

  retrieveTodos(): void {
    this.TodoService.getAll()
      .subscribe(
        data => {
          this.todo = data;
          console.log(data);
          console.log(this.currentTodo)

        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveTodos();
    this.currentTodo = {};
    this.currentIndex = -1;
  }

  setActiveTodo(todo: Todo, index: number): void {
    this,this.currentTodo = todo;
    this.currentIndex = index;
  }
}