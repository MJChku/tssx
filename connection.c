#include "tssx/connection.h"
#include "tssx/buffer.h"
#include "tssx/shared_memory.h"

void setup_connection(Connection* connection, int buffer_size) {
	void* shared_memory;

	shared_memory = attach_segment(connection->segment_id);

	create_server_buffer(connection, shared_memory, buffer_size);
	create_client_buffer(connection, shared_memory, buffer_size);
}

void create_server_buffer(Connection* connection,
													void* shared_memory,
													int buffer_size) {
	connection->server_buffer = create_buffer(shared_memory, buffer_size);
}

void create_client_buffer(Connection* connection,
													void* shared_memory,
													int buffer_size) {
	shared_memory += segment_size(connection->server_buffer);
	connection->client_buffer = create_buffer(shared_memory, buffer_size);
}