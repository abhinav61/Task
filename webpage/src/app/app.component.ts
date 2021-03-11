import { Component, OnInit } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [UserService]
})
export class AppComponent implements OnInit {
  title = 'webpage';
  register;
  input;
  registers;
  confirm_password:any;

  constructor(private userService: UserService){}
 

  ngOnInit(){
    this.register = {
      first_name : '',
      last_name :'',
      company_name: '',
      email_id :'',
      phone_number: '',
      password: '',
      confirm_password: ''


    };
    this.input = {
      email_id:'',
      password: ''
    }
    this.registers={
      first_name:'',
      last_name:'',
      phone_number:''

    }
    
  }
  newregister(){
    this.userService.newregister(this.register).subscribe(
      Response =>{
        alert('User' + this.register.first_name + 'has been created successfully!')
      },
      error => console.error('errors',error)
    )
  

  }
  onlogin(){
    this.userService.onlogin(this.input).subscribe(
      Response =>{
        console.log();
        alert('User' + this.input.first_name + 'user has been logged in succesfully!')
      }, 
      error => console.error('errors',error)
    )
    
  


  }
  update(){
    this.userService.update(this.registers).subscribe(
      Response =>{
        console.log();
        alert('User' + this.registers.first_name + 'user has been successfully updated!')
      }, 
      error => console.error('errors',error)
    )
  }
}
