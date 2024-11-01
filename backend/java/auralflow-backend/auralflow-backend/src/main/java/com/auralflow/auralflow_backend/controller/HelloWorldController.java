package com.auralflow.auralflow_backend.controller;

import com.auralflow.auralflow_backend.kafka.producer.HelloWorldProducerService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {
    private HelloWorldProducerService kafkaProducerService;

    public HelloWorldController(HelloWorldProducerService kafkaProducerService) {
        this.kafkaProducerService = kafkaProducerService;
    }

    @GetMapping("/publish")
    public String publishMessage() {
        kafkaProducerService.sendMessage();
        return "Message published!";
    }
}
