import { Model } from 'mongoose';
import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { User } from '../../../../shared/dto/user.dto';
import {CreateUserDto} from '../../../../shared/dto/create-user.dto';
@Injectable()
export class UsersService {
    constructor(@InjectModel('User') private readonly userModel: Model<User>) {}

    async create(createUserDto: CreateUserDto): Promise<User> {
        const createdUser = new this.userModel(createUserDto);
        return await createdUser.save();
      }

    async findAll(): Promise<User[]> {
      return await this.userModel.find().exec();
    }
}
