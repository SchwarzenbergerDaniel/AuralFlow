package com.auralflow.auralflow_backend.kafka.producer;

import com.auralflow.auralflow_backend.kafka.config.KafkaTopic;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class HelloWorldProducerService {
    private final KafkaTemplate<String, String> kafkaTemplate;

    @Autowired
    public HelloWorldProducerService(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void sendMessage(String message) {
        kafkaTemplate.send(KafkaTopic.HELLO_WORLD_TOPIC, "key", message);
    }


}
