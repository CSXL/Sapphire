use std::{error::Error, str::FromStr};

use httpmock::MockServer;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct Response {
    pub transcript: String,
    pub sent_tokens: Vec<String>,
}

// Retrieves the transcript from the API based on the video ID
pub async fn get_transcript(baseurl: String, video_id: String) -> String {
    let body = call_api(baseurl, video_id.to_string()).await.unwrap();
    return body.transcript;
}

// Retrieves the sentence tokens from the API based on the video ID
pub async fn get_sent_tokens(baseurl: String, video_id: String) -> Vec<String> {
    let body = call_api(baseurl, video_id.to_string()).await.unwrap();
    return body.sent_tokens;
}

// Calls the API and returns the response
pub async fn call_api(baseurl: String, video_id: String) -> Result<Response, Box<dyn Error>> {
    let url = format!("{}/get_transcript/{}", baseurl, video_id);

    // Make a GET request to the API
    let body = reqwest::get(url).await?.text().await?;

    // Deserialize the API response into a Response struct
    let res = serialize_response(body).await?;

    Ok(res)
}

// Deserializes the JSON response into a Response struct
async fn serialize_response(body: String) -> Result<Response, serde_json::Error> {
    let response: Response = serde_json::from_str(&body)?;

    Ok(response)
}

#[cfg(test)]
#[tokio::test]
async fn test_call_api() {
    let server = MockServer::start();
    let mock = server.mock(|when, then| {
        when.method(httpmock::Method::GET)
            .path("/get_transcript/8mAITcNt710");
        then.status(200)
            .header("Content-Type", "application/json")
            .body(r#"{"transcript":"Hello world","sent_tokens":["hello", "world"]}"#);
    });
    let baseurl = server.base_url();
    let body = call_api(baseurl,"8mAITcNt710".to_string()).await.unwrap();
}

#[tokio::test]
async fn test_get_transcript() {
    let server = MockServer::start();
    let mock = server.mock(|when, then| {
        when.method(httpmock::Method::GET)
            .path("/get_transcript/8mAITcNt710");
        then.status(200)
            .header("Content-Type", "application/json")
            .body(r#"{"transcript":"Hello world","sent_tokens":["hello", "world"]}"#);
    });
    let baseurl = server.base_url();
    let body = get_transcript(baseurl,"8mAITcNt710".to_string()).await;
    assert_eq!(body, "Hello world");
}

#[tokio::test]
async fn test_get_sent_tokens(){
    let server = MockServer::start();
    let mock = server.mock(|when, then| {
        when.method(httpmock::Method::GET)
        .path("/get_transcript/8mAITcNt710");
        then.status(200)
        .header("Content-Type", "application/json")
        .body(r#"{"transcript":"Hello world","sent_tokens":["hello", "world"]}"#);
        
    }
    );
    let baseurl = server.base_url();
        let body = get_sent_tokens(baseurl,"8mAITcNt710".to_string()).await;
        let mut expected: Vec<String> = vec![];

        expected.push(String::from("hello"));
        expected.push(String::from("world"));
     assert_eq!(body, expected);
}