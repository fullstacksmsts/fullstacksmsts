import React from 'react';

const RelatedPosts = ({ posts }) => {
  if (!posts || posts.length === 0) {
    return null;
  }

  return (
    <div className="mb-12">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Related Articles</h2>
      <div className="grid md:grid-cols-3 gap-6">
        {posts.map(post => (
          <div key={post.id} className="bg-white border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow">
            <a href={`/blog/${post.id}`}>
              <img 
                src={post.featuredImage} 
                alt={post.title} 
                className="w-full h-48 object-cover"
              />
            </a>
            <div className="p-4">
              <span className="text-xs font-medium text-blue-600">{post.category}</span>
              <a href={`/blog/${post.id}`} className="block mt-2">
                <h3 className="text-lg font-semibold text-gray-900 hover:text-blue-600">{post.title}</h3>
              </a>
              <p className="text-sm text-gray-500 mt-1">{post.readTime}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RelatedPosts;
