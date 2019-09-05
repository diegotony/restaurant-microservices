import { Controller } from '@nestjs/common';
import { MessagePattern } from '@nestjs/microservices';
import { CreateUserDto } from '../../../../shared/dto/create-user.dto';
import { UsersService } from './users.service';
import { User } from '../../../../shared/dto/user.dto';

@Controller()
export class UsersController {
    constructor(private readonly usersService: UsersService) { }
    @MessagePattern({ cmd: 'create' })
    async create(dto: CreateUserDto) {
      // TODO: map to UserDTO
      return (await this.usersService.create(dto));
    }

    @MessagePattern({ cmd: 'findAll' })
    async findAll(): Promise<User[]> {
      return (await this.usersService.findAll()).map(v => ({name: v.name, email: v.email, password: v.password}));
    }
}
