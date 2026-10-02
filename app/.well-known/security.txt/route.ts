export function GET() {
  const body = [
    "Contact: mailto:hello@hackergovind.dev",
    "Expires: 2027-10-02T00:00:00.000Z",
    "Preferred-Languages: en",
  ].join("\n");
  return new Response(body, {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
