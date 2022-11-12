import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
// import { HomeComponent } from './home/home.component';

import { TodoListComponent } from './todo-list/todo-list.component';
import { TodoDetailsComponent } from './todo-details/todo-details.component';
import { AddTodoComponent } from './add-todo/add-todo.component';

const routes: Routes = [
  // { path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'todo', component: TodoListComponent },
  { path: 'todo/:id', component: TodoDetailsComponent },
  { path: 'add', component: AddTodoComponent },
  { path: '', redirectTo: 'todo', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }