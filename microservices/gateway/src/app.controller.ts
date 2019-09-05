import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';
import { ClientProxy, ClientProxyFactory, Transport } from '@nestjs/microservices';

@Controller()
export class AppController {
  private readonly client: ClientProxy;

  constructor(private readonly appService: AppService) {
    this.client = ClientProxyFactory.create({
      transport: Transport.TCP
    });
  }
  // @Get('all')
  // getclients() {
  //   return this.client.send<string[]>({cmd: 'LIST_MOVIES'}, []);
  // }
}
