import { Pipe, PipeTransform } from '@angular/core';
import { IfObservable } from 'rxjs/observable/IfObservable';

@Pipe({
  name: 'reverse'
})
export class ReversePipe implements PipeTransform {

  transform(value: any, args?: any): any {
    if (!value) {
      return;
    }
    return value.reverse();
  }

}
