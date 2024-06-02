// Reject the promises
export default function uploadPhoto(filename) {
    return Promise.reject(
        new Error(`${filename} cannot be processed`),
    );
}
