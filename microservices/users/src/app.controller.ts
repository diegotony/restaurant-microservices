import { Controller } from '@nestjs/common';
import { MessagePattern} from '@nestjs/microservices';
// import { AppService } from './app.service';
@Controller()
export class AppController {
  // @Client({ transport: Transport.TCP, options: { port: 3001 } })
  // private db: ClientProxy;
  // constructor(private readonly appService: AppService) {}
  // @MessagePattern({cmd: 'LIST_MOVIES'})
  // getMovies(): string[] {
  //   return ['Pulp Fiction', 'Titanic', 'Matrix'];
  // }
}