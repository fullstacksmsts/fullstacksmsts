import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import RelatedPosts from './RelatedPosts';
import CommentSection from './CommentSection';
import { blogPosts } from '../../data/blogPosts';

const BlogPost = () => {
  const { postId } = useParams();
  const [post, setPost] = useState(null);
  const [relatedPosts, setRelatedPosts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // In a real implementation, this would fetch from an API
    const fetchPost = () => {
      setIsLoading(true);
      
      // Find the current post
      const currentPost = blogPosts.find(post => post.id === postId);
      
      if (currentPost) {
        // Get related posts
        const related = currentPost.related
          .map(relId => blogPosts.find(p => p.id === relId))
          .filter(p => p !== undefined);
          
        setPost(currentPost);
        setRelatedPosts(related);
      }
      
      setIsLoading(false);
    };

    fetchPost();
  }, [postId]);

  // Function to convert markdown content to HTML (simplified version)
  const renderContent = (markdown) => {
    // In a real implementation, you would use a library like marked or react-markdown
    // This is a simplified example
    const html = markdown
      .replace(/^# (.*$)/gm, '<h1>$1</h1>')
      .replace(/^## (.*$)/gm, '<h2>$1</h2>')
      .replace(/\*\*(.*)\*\*/gm, '<strong>$1</strong>')
      .replace(/\- (.*$)/gm, '<li>$1</li>')
      .replace(/\n\n/gm, '<br><br>');
      
    return <div dangerouslySetInnerHTML={{ __html: html }} />;
  };

  if (isLoading) {
    return <div className="flex justify-center items-center h-64">Loading...</div>;
  }

  if (!post) {
    return <div className="text-center py-12">Blog post not found</div>;
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      {/* Structured Data for SEO */}
      <script type="application/ld+json">
        {JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BlogPosting",
          "headline": post.title,
          "description": post.subtitle,
          "image": post.featuredImage,
          "author": {
            "@type": "Person",
            "name": post.author
          },
          "publisher": {
            "@type": "Organization",
            "name": "FullStack SMSTS",
            "logo": {
              "@type": "ImageObject",
              "url": "https://fullstacksmsts.co.uk/logo.png"
            }
          },
          "datePublished": post.date,
          "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": `https://fullstacksmsts.co.uk/blog/${post.id}`
          }
        })}
      </script>
      
      {/* Breadcrumbs */}
      <nav className="text-sm text-gray-500 mb-6" aria-label="Breadcrumb">
        <ol className="flex">
          <li><a href="/" className="hover:text-blue-600">Home</a></li>
          <li className="mx-2">/</li>
          <li><a href="/blog" className="hover:text-blue-600">Blog</a></li>
          <li className="mx-2">/</li>
          <li className="text-gray-700">{post.title}</li>
        </ol>
      </nav>
      
      {/* Featured Image */}
      <div className="mb-6">
        <img 
          src={post.featuredImage} 
          alt={post.title} 
          className="w-full h-auto rounded-lg shadow-md"
        />
      </div>
      
      {/* Post Header */}
      <header className="mb-8">
        <div className="flex items-center text-sm text-gray-500 mb-2">
          <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded">{post.category}</span>
          <span className="mx-2">•</span>
          <span>{post.readTime}</span>
        </div>
        <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-2">{post.title}</h1>
        <p className="text-xl text-gray-600 mb-4">{post.subtitle}</p>
        <div className="flex items-center">
          <img src="/api/placeholder/48/48" alt={post.author} className="w-12 h-12 rounded-full" />
          <div className="ml-3">
            <p className="text-gray-900 font-medium">{post.author}</p>
            <p className="text-gray-500 text-sm">{post.date}</p>
          </div>
        </div>
      </header>
      
      {/* Main Content */}
      <article className="prose max-w-none mb-12">
        {renderContent(post.content)}
      </article>
      
      {/* CTA Section */}
      <div className="bg-blue-50 border-l-4 border-blue-500 p-6 rounded-lg mb-12">
        <h3 className="text-xl font-bold text-blue-800 mb-2">Book Your SMSTS Course Today</h3>
        <p className="mb-4">With a 98% pass rate and competitive pricing of just £360+VAT, fullstacksmsts.co.uk is the trusted choice for SMSTS training across the UK.</p>
        <div className="flex flex-col sm:flex-row gap-4">
          <a href="/book-course" className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-6 rounded-lg text-center transition duration-150">
            Book SMSTS Course
          </a>
          <a href="/contact" className="bg-white hover:bg-gray-100 text-blue-600 border border-blue-600 font-medium py-2 px-6 rounded-lg text-center transition duration-150">
            Request a Callback
          </a>
        </div>
      </div>
      
      {/* Related Posts */}
      {relatedPosts.length > 0 && (
        <RelatedPosts posts={relatedPosts} />
      )}
      
      {/* Comment Section */}
      <CommentSection />
    </div>
  );
};

export default BlogPost;
