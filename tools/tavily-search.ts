import { z } from 'zod';

export const schema = z.object({
  query: z.string().describe('Search query'),
  max_results: z.number().optional().default(5).describe('Max results to return'),
});

export default async function ({ query, max_results = 5 }: z.infer<typeof schema>) {
  const apiKey = process.env.TAVILY_API_KEY;
  if (!apiKey) throw new Error('TAVILY_API_KEY not set');

  const response = await fetch('https://api.tavily.com/search', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      api_key: apiKey,
      query,
      max_results,
      include_answer: true,
      include_raw_content: false,
    }),
  });

  const data = await response.json();
  
  return {
    answer: data.answer,
    results: data.results?.map((r: any) => ({
      title: r.title,
      url: r.url,
      content: r.content,
    })) || [],
  };
}
