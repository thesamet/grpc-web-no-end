require('grpc-web');

const {Req} = require('./gen/myservice_pb.js');
const {TestServiceClient} = require('./gen/myservice_grpc_web_pb.js');

var service = new TestServiceClient("http://localhost:8081");

var request = new Req()
request.setPayload("Hello!");
x = service.serverStreaming(request, {}, function(err, response) {
    if (response) {
        console.log(response.toObject());
    } else {
        console.log(err);
    }
});
x.on('data', function(data) {
    console.log(data.toObject());
});
x.on('end', function(data) {
    console.log('end');
});
