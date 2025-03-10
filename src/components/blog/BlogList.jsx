import React from 'react';
import { Link } from 'react-router-dom';
import { blogPosts } from '../../data/blogPosts';

const BlogList = () => {
  return (
    <div className="max-w-7xl mx-auto">
      {/* Page Header */}
      <div className="mb-12 text-center">
        <h1 className="text-3xl md:text-4xl font-bold text-[var(--primary-blue)] mb-4">
          SMSTS Training Blog
        </h1>
        <p className="text-lg text-gray-600 max-w-3xl mx-auto">
          Expert insights, guides, and resources for construction site managers and safety professionals.
          Learn about SMSTS courses, certification, and best practices.
        </p>
      </div>
      
      {/* Featured Post */}
      {blogPosts.length > 0 && (
        <div className="mb-16">
          <div className="bg-white rounded-xl shadow-lg overflow-hidden">
            <div className="md:flex">
              <div className="md:flex-shrink-0 md:w-1/2">
                <img 
                  src={blogPosts[0].featuredImage} 
                  alt={blogPosts[0].title} 
                  className="h-64 w-full object-cover md:h-full"
                />
              </div>
              <div className="p-8 md:w-1/2">
                <div className="flex items-center text-sm text-gray-500 mb-2">
                  <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded">{blogPosts[0].category}</span>
                  <span className="mx-2">•</span>
                  <span>{blogPosts[0].readTime}</span>
                </div>
                <Link to={`/blog/${blogPosts[0].id}`} className="block mt-1">
                  <h2 className="text-2xl font-bold text-gray-900 hover:text-[var(--cta-orange)]">
                    {blogPosts[0].title}
                  </h2>
                </Link>
                <p className="mt-3 text-gray-600">
                  {blogPosts[0].subtitle}
                </p>
                <div className="mt-6 flex items-center">
                  <div className="flex-shrink-0">
                    <img src="/api/placeholder/40/40" alt={blogPosts[0].author} className="h-10 w-10 rounded-full" />
                  </div>
                  <div className="ml-3">
                    <p className="text-sm font-medium text-gray-900">{blogPosts[0].author}</p>
                    <p className="text-sm text-gray-500">{blogPosts[0].date}</p>
                  </div>
                </div>
                <div className="mt-6">
                  <Link 
                    to={`/blog/${blogPosts[0].id}`} 
                    className="text-[var(--cta-orange)] hover:text-[var(--orange-accent)] font-medium flex items-center"
                  >
                    Read full article
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                      <path fillRule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                    </svg>
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
      
      {/* Blog Post Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {blogPosts.slice(1).map(post => (
          <div key={post.id} className="bg-white rounded-xl shadow-lg overflow-hidden transition-transform hover:scale-105">
            <Link to={`/blog/${post.id}`}>
              <img 
                src={post.featuredImage} 
                alt={post.title} 
                className="w-full h-48 object-cover"
              />
            </Link>
            <div className="p-6">
              <div className="flex items-center text-sm text-gray-500 mb-2">
                <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded">{post.category}</span>
                <span className="mx-2">•</span>
                <span>{post.readTime}</span>
              </div>
              <Link to={`/blog/${post.id}`} className="block mt-2">
                <h3 className="text-xl font-bold text-gray-900 hover:text-[var(--cta-orange)]">{post.title}</h3>
              </Link>
              <p className="mt-3 text-gray-600 line-clamp-3">
                {post.subtitle}
              </p>
              <div className="mt-6 flex items-center">
                <div className="flex-shrink-0">
                  <img src="/api/placeholder/40/40" alt={post.author} className="h-8 w-8 rounded-full" />
                </div>
                <div className="ml-3">
                  <p className="text-sm font-medium text-gray-900">{post.author}</p>
                  <p className="text-sm text-gray-500">{post.date}</p>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
      
      {/* CTA Section */}
      <div className="mt-16 bg-[var(--primary-blue)] text-white rounded-xl p-8 shadow-lg">
        <div className="md:flex items-center justify-between">
          <div className="md:w-2/3">
            <h2 className="text-2xl font-bold mb-4">Ready to advance your construction career?</h2>
            <p className="mb-6 md:mb-0">
              Book your SMSTS course today with fullstacksmsts.co.uk. With a 98% pass rate and competitive pricing of just £360+VAT, we're the trusted choice for SMSTS training across the UK.
            </p>
          </div>
          <div className="md:w-1/3 text-center md:text-right">
            <Link 
              to="/book-course" 
              className="inline-block bg-[var(--cta-orange)] hover:bg-[var(--orange-accent)] text-white font-medium py-3 px-6 rounded-lg transition duration-150"
            >
              Book SMSTS Course
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BlogList;
