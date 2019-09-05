import { Injectable } from '@nestjs/common';

import {
    ClientProxy,
    Client,
    Transport,
  } from '@nestjs/microservices';

import { Observable } from 'rxjs';
import {CreateUserDto} from '../../../../shared/dto/create-user.dto';
import {User} from '../../../../shared/dto/user.dto';

@Injectable()
export class UsersService {
  @Client({ transport: Transport.TCP, options: { port: 3003 } })
  private client: ClientProxy;
  public create(dto: CreateUserDto): Observable<any> {
    return this.client.send({ cmd: 'create' }, dto);
  }

  public findAll(): Observable<User[]> {
    return this.client.send({ cmd: 'findAll' }, '');
  }

}
