// hello-world.component.ts
import { Component, OnInit, ElementRef } from '@angular/core';
import { gsap } from 'gsap';

@Component({
  selector: 'app-hello-world',
  templateUrl: './hello-world.component.html',
  styleUrls: ['./hello-world.component.css'],
  standalone: true
})
export class HelloWorldComponent implements OnInit {
  constructor(private elementRef: ElementRef) {}

  ngOnInit(): void {
    gsap.from(this.elementRef.nativeElement.querySelector('#helloText'), {
      duration: 2,
      opacity: 0,
      y: -50,
      ease: 'bounce'
    });
  }
}
