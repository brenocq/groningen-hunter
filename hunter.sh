#!/bin/bash
VERSION="1.0.0"
ENV_FILE="src/.env"

display_help() {
    echo "Usage: $0 {--run|--version|--build|--set-max <value>|--set-min <value>|--set-chat-id <value>|--set-bot-token <value>|--show-config|--help}"
    echo
    echo "Options:"
    echo "  --run                   Build the Docker image and run the container"
    echo "  --version               Print the Docker image version and package versions"
    echo "  --build                 Build the Docker image"
    echo "  --set-max <value>       Set the maximum price in the configuration"
    echo "  --set-min <value>       Set the minimum price in the configuration"
    echo "  --set-chat-id <value>   Set the chat ID in the configuration"
    echo "  --set-bot-token <value> Set the bot token in the configuration"
    echo "  --show-config           Show the current configuration"
    echo "  --help                  Display this help message"
}

# Build the Docker image
build_image() {
    docker build -t groningen-hunter .
}

# Run the Docker container
run_container() {
    docker run -it --rm --name groningen-hunter-container groningen-hunter
}

# Print the groningen hunter version and versions inside docker image
print_version() {
    echo "Groningen Hunter $VERSION"
    echo
    docker run --rm groningen-hunter google-chrome-stable --version
    docker run --rm groningen-hunter pip freeze
}

# Show the current configuration
show_config() {
    echo "Current Configuration:"
    echo
    cat $ENV_FILE
}

# Set a configuration value
set_config() {
    key=$1
    value=$2
    if [ -f "$ENV_FILE" ]; then
        # Update the existing value or add it if not present
        if grep -q "^$key=" "$ENV_FILE"; then
            sed -i "s/^$key=.*/$key=\"$value\"/" "$ENV_FILE"
        else
            echo "$key=\"$value\"" >> "$ENV_FILE"
        fi
    else
        # Create the .env file and add the key-value pair
        echo "$key=\"$value\"" > "$ENV_FILE"
    fi
}

# Check argument
case "$1" in
    --run)
        build_image && run_container
        ;;
    --version)
        print_version
        ;;
    --build)
        build_image
        ;;
    --set-max)
        set_config "MAXIMUM_PRICE" "$2"
        ;;
    --set-min)
        set_config "MINIMUM_PRICE" "$2"
        ;;
    --set-chat-id)
        set_config "CHAT_ID" "$2"
        ;;
    --set-bot-token)
        set_config "BOT_TOKEN" "$2"
        ;;
    --show-config)
        show_config
        ;;
    --help)
        display_help
        ;;
    *)
        echo "Invalid option: $1"
        display_help
        ;;
esac
