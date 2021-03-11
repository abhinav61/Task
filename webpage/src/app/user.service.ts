import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) {}

  newregister(userData): Observable<any>{
    return this.http.post('http://127.0.0.1:8000/api/users/', userData)
  }
  onlogin(userData): Observable<any>{
    return this.http.post('http://127.0.0.1:8000/api/auth/', userData)
  }
  onforgot(userData):Observable<any>{
    return this.http.post('http://127.0.0.1:8000/api/auth/password/',userData)

  }
  update(userData):Observable<any>{
    return this.http.post('http://127.0.0.1:8000/api/update',userData)
}
}