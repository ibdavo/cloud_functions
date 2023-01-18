# README

## Documentation
https://lucid.app/lucidchart/1fb615e6-2711-43c8-98cb-de6b6bf03a63/edit?viewport_loc=-203%2C105%2C2219%2C996%2C0_0&invitationId=inv_8b22ab09-173b-4e87-8836-3aef82842458

## Pre-installation requirements
    -[] gcloud CLI:  https://cloud.google.com/sdk/docs/install
    
    Emulators to install:
        -[] Cloud Functions Emulator:  https://cloud.google.com/functions/docs/emulator
        -[] Cloud Pub/Sub Emulator:  https://cloud.google.com/pubsub/docs/emulator
            The pubsub emulator requires Java JRE 7+ to be installed. 
                curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u112-b15/jre-8u112-macosx-x64.dmg > jre-8u112-macosx-x64.dmg
                curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u351-b15/jre-8u351-macosx-x64.dmg > jre-8u351-macosx-x64.dmg
        -[] 

## Start emulator
    $ gcloud beta emulators pubsub start --project=testproj --host-port='localhost:7001'
        You need the [pubsub-emulator] component to use the Google Cloud
        Pub/Sub emulator.


        Your current Google Cloud CLI version is: 410.0.0
        Installing components from version: 410.0.0

        ┌─────────────────────────────────────────────┐
        │     These components will be installed.     │
        ├────────────────────────┬─────────┬──────────┤
        │          Name          │ Version │   Size   │
        ├────────────────────────┼─────────┼──────────┤
        │ Cloud Pub/Sub Emulator │   0.7.1 │ 62.4 MiB │
        └────────────────────────┴─────────┴──────────┘

        For the latest full release notes, please visit:
        https://cloud.google.com/sdk/release_notes

        Do you want to continue (Y/n)?

        .
        .
        .
        <!-- Restart emulator -->
    $ gcloud beta emulators pubsub start --project=testproj --host-port='localhost:7001'
            Executing: /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/platform/pubsub-emulator/bin/cloud-pubsub-emulator --host=localhost --port=7001
            [pubsub] This is the Google Pub/Sub fake.
            [pubsub] Implementation may be incomplete or differ from the real system.
            [pubsub] Jan 11, 2023 3:45:17 PM com.google.cloud.pubsub.testing.v1.Main main
            [pubsub] INFO: IAM integration is disabled. IAM policy methods and ACL checks are not supported
            [pubsub] SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
            [pubsub] SLF4J: Defaulting to no-operation (NOP) logger implementation
            [pubsub] SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
            [pubsub] Jan 11, 2023 3:45:18 PM com.google.cloud.pubsub.testing.v1.Main main
            [pubsub] INFO: Server started, listening on 7001

## Setup pubsub environment var
    ### In a new terminal, same directory, run:
    $ (gcloud beta emulators pubsub env-init)

## Create a topic "main-topic"
    $ curl -s -X PUT 'http://localhost:7001/v1/projects/testproj/topics/topic-a'

            {
                "name": "projects/testproj/topics/topic-a"
            }
## Create a subscription
    $ curl -s -X PUT 'http://localhost:7001/v1/projects/testproj/subscriptions/subscr_signals' \
        -H 'Content-Type: application/json' \
        --data '{"topic":"projects/testproj/topics/topic-a","pushConfig":{"pushEndpoint":"http://localhost:8082/projects/testproj/topics/topic-a"},"ackDeadlineSeconds": 5}'

                {
                "name": "projects/testproj/subscriptions/subscr_signals",
                "topic": "projects/testproj/topics/topic-a",
                "pushConfig": {
                    "pushEndpoint": "http://localhost:8082/projects/testproj/topics/main-topic"
                },
                "ackDeadlineSeconds": 5,
                "messageRetentionDuration": "604800s"
                }        

## Test topic
    $ curl -s -X POST 'http://localhost:7001/v1/projects/testproj/topics/topic-a:publish' \
    -H 'Content-Type: application/json' \
    --data '{"messages":[{"data":"eyJmb28iOiJiYXIifQ=="}]}'

## Start Cloud Functions Emulator for (function1)
    $ cd f1
    $ pipenv setup
    $ pipenv install
    $ functions-framework --debug --source=function1.py --target=main_f1 --port=8080

    