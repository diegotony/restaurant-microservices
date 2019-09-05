import { Controller, Get, Post, Body } from '@nestjs/common';
import {CreateUserDto} from '../../../../shared/dto/create-user.dto';
import {User} from '../../../../shared/dto/user.dto';
import { Observable } from 'rxjs';
import { UsersService } from './users.service';
@Controller('api/users')
export class UsersController {
    public constructor(
        private readonly usersService: UsersService,
      ) { }

      @Post()
      public create(@Body() dto: CreateUserDto): Observable<any> {
        console.log(dto);
        return this.usersService.create(dto);
      }

      @Get()
      public findAll(): Observable<User[]> {
        return this.usersService.findAll();
      }
}
