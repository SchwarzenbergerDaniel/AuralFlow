package com.auralflow.auralflow_backend.kafka.producer;

import com.auralflow.auralflow_backend.kafka.config.KafkaTopic;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.time.Instant;

import com.auralflow.avro.PlayEvent;

@Service
public class HelloWorldProducerService {
    private final KafkaTemplate<String, PlayEvent> kafkaTemplate;

    @Autowired
    public HelloWorldProducerService(KafkaTemplate<String, PlayEvent> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void sendMessage() {
        String key = "userID" + "-" + Timestamp.from(Instant.now()).toString();
        PlayEvent event = PlayEvent.newBuilder()
                .setTimestamp(Instant.now())
                .setSongId("SongId")
                .setUserId("userId")
                .build();
        kafkaTemplate.send(KafkaTopic.HELLO_WORLD_TOPIC, key, event);
    }


}
