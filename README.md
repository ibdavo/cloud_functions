# README
This is a simple example of how to use the Cloud Functions Emulator to build and test a Cloud Functions.   It is divided into two lessons.  The first is the building and testing of a single Cloud Function.  The second is the building and testing two Cloud Functions that communicate via Pub / Sub.

## Architecture documentation
    Lucid document is located [here](https://lucid.app/lucidchart/1fb615e6-2711-43c8-98cb-de6b6bf03a63/edit?viewport_loc=-203%2C105%2C2219%2C996%2C0_0&invitationId=inv_8b22ab09-173b-4e87-8836-3aef82842458)

## Clone Repo
    $ git clone https://github.com/ibdavo/cloud_functions.git

## Pre-installation requirements
    -[] gcloud CLI:  https://cloud.google.com/sdk/docs/install
    
    Emulators to install:
        -[] Cloud Functions Emulator:  https://cloud.google.com/functions/docs/emulator
        -[] Cloud Pub/Sub Emulator:  https://cloud.google.com/pubsub/docs/emulator
            The pubsub emulator requires Java JRE 7+ to be installed. 



# Lesson A:  Single Cloud Function
## Clone example repo
    $ git clone https://github.com/ibdavo/cloud_functions.git
    $ cd cloud_functions/lesson_a
## Start Cloud Functions Emulator
    $ pipenv install
    $ pipenv shell
    $ cd cloud_functions/f1
    $ functions-framework --debug --source=main.py --target=main --port=8080

## Test Cloud Function (start new terminal)
    $ curl -X POST -H "Content-Type: application/json" -d '{"name":"Dave"}' http://localhost:8080

            Hello World

## Deploy cloud function to Google cloud
### Use gcloud to authorize login
    $ gcloud auth login

### Use gcloud to set project
    $ gcloud config set project testproj
    
    $ gcloud functions deploy f1 --runtime python39 --trigger-http --project=testproj --region=us-central1

            Deploying function (may take a while - up to 2 minutes)...done.
            Available memory allocated: 256MB
            Function URL (f1): https://us-central1-testproj.cloudfunctions.net/f1
## Wrap-up and exit.  Stop emulator, exit pipenv shell
    $ control-C
    $ exit



# Lesson B:  Two Cloud Functions communicating via Pub / Sub

### A word of caution.  Using the pubsub emulator can have precarious side effects. Please take note of the cleanup steps at the end of this lesson.  If you do not, you will be haunted by the ghost of Christmas past.  You have been warned.

## Start emulator in new terminal
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

## Setup pubsub environment variable in new terminal
    $ (gcloud beta emulators pubsub env-init)

## Create a TOPIC "main-topic"
    $ curl -s -X PUT 'http://localhost:7001/v1/projects/testproj/topics/topic-a'

            {
                "name": "projects/testproj/topics/topic-a"
            }

## Create a SUBSCRIPTION
    $ curl -s -X PUT 'http://localhost:7001/v1/projects/testproj/subscriptions/subscr_f2' \
        -H 'Content-Type: application/json' \
        --data '{"topic":"projects/testproj/topics/topic-a","pushConfig":{"pushEndpoint":"http://localhost:8082/projects/testproj/topics/topic-a"},"ackDeadlineSeconds": 5}'

                {
                "name": "projects/testproj/subscriptions/topic-a",
                "topic": "projects/testproj/topics/topic-a",
                "pushConfig": {
                    "pushEndpoint": "http://localhost:8082/projects/testproj/topics/topic-a"
                },
                "ackDeadlineSeconds": 5,
                "messageRetentionDuration": "604800s"
                }   

## Test publication to topic "topic-a"
    $ curl -s -X POST 'http://localhost:7001/v1/projects/testproj/topics/topic-a:publish' \
    -H 'Content-Type: application/json' \
    --data '{"messages":[{"data":"eyJmb28iOiJiYXIifQ=="}]}'

## Start Cloud Functions Emulator for (function1)
    $ cd lesson_b/f1
    $ pipenv install
    $ pipenv shell
    $ export PUBSUB_EMULATOR_HOST=localhost:7001
    $ functions-framework --debug --source=function1.py --target=main_f1 --port=8081

## Start Cloud Functions Emulator for (function2)
    $ cd cd lesson_b/f2
    $ pipenv install
    $ pipenv shell
    $ export PUBSUB_EMULATOR_HOST=localhost:7001
    $ functions-framework --debug --source=function2.py --target=main_f2 --port=8082

## Test Cloud Function (start new terminal)
    $ curl -X POST -H "Content-Type: application/json" -d '{"name":"Dave"}' http://localhost:8081

            Hello Dave

## Wrap-up and exit.  Stop emulator, exit pipenv shell
### In the emulator terminal, control-C to stop the emulator
    $ control-C
### Check if pubsub emulator is still running
    $ ps -aux | grep pubsub
### If it is still running, kill it
### In the pipenv shell (function-1), exit shell, exit terminal
    $ exit
    $ exit
### In the pipenv shell (function-2), exit shell, exit terminal
    $ exit
    $ exit


    
